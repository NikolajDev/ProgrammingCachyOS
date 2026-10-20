import 'package:flame/game.dart';
import 'package:flame_forge2d/flame_forge2d.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'game_state.dart';

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (context) => GameState(),
      child: const PlinkoGameApp(),
    ),
  );
}

class PlinkoGameApp extends StatelessWidget {
  const PlinkoGameApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark(),
      home: const MainGameScreen(),
    );
  }
}

class MainGameScreen extends StatelessWidget {
  const MainGameScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final gameState = Provider.of<GameState>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text("Peniaze: \$${gameState.money.toStringAsFixed(1)} | Násobič: x${gameState.multiplier}"),
      ),
      body: Row(
        children: [
          // Ľavá strana: Plinko herná plocha (Flame)
          Expanded(
            flex: 2,
            child: GameWidget(game: PlinkoWorld(gameState)),
          ),
          // Pravá strana: Obchod a 4x3 mriežka
          Expanded(
            flex: 1,
            child: Container(
              padding: const EdgeInsets.all(8.0),
              color: Colors.black26,
              child: Column(
                children: [
                  const Text("Obchod / Vylepšenia", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 10),
                  ElevatedButton(
                    onPressed: () => gameState.buyItem("+1", 10.0),
                    child: const Text("Kúpiť +1 (Cena: \$10)"),
                  ),
                  ElevatedButton(
                    onPressed: () => gameState.buyItem("x1.1", 25.0),
                    child: const Text("Kúpiť x1.1 (Cena: \$25)"),
                  ),
                  const Divider(height: 30),
                  const Text("Mriežka (4x3)", style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 10),
                  Expanded(
                    child: GridView.builder(
                      itemCount: 12,
                      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                        crossAxisCount: 3,
                        crossAxisSpacing: 8,
                        mainAxisSpacing: 8,
                      ),
                      itemBuilder: (context, index) {
                        final item = gameState.grid[index];
                        return DragTarget<int>(
                          onAcceptWithDetails: (details) {
                            gameState.mergeItems(details.data, index);
                          },
                          builder: (context, candidateData, rejectedData) {
                            if (item == null) {
                              return Container(
                                decoration: BoxDecoration(
                                  border: Border.all(color: Colors.white24),
                                  borderRadius: BorderRadius.circular(8),
                                ),
                              );
                            }
                            return Draggable<int>(
                              data: index,
                              feedback: Material(
                                color: Colors.transparent,
                                child: Container(
                                  width: 50,
                                  height: 50,
                                  decoration: BoxDecoration(
                                    color: Colors.blue,
                                    borderRadius: BorderRadius.circular(8),
                                  ),
                                  child: Center(child: Text("${item['type']} Lvl ${item['level']}")),
                                ),
                              ),
                              child: Container(
                                decoration: BoxDecoration(
                                  color: Colors.blueAccent,
                                  borderRadius: BorderRadius.circular(8),
                                ),
                                child: Center(
                                  child: Text(
                                    "${item['type']}\nLvl ${item['level']}",
                                    textAlign: TextAlign.center,
                                    style: const TextStyle(fontSize: 12),
                                  ),
                                ),
                              ),
                            );
                          },
                        );
                      },
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

// Flame Forge2D svet pre fyziku padania
class PlinkoWorld extends Forge2DGame {
  final GameState gameState;
  PlinkoWorld(this.gameState) : super(gravity: Vector2(0, 10));

  @override
  Future<void> onLoad() async {
    await super.onLoad();
    camera.viewfinder.zoom = 20;
    add(Ball(Vector2(0, -15), gameState));
  }
}

class Ball extends BodyComponent {
  final GameState gameState;
  Ball(Vector2 position, this.gameState) : super(
    bodyDef: BodyDef(
      type: BodyType.dynamic,
      position: position,
    ),
    shapeSpecs: [
      ShapeSpec(
        Circle(radius: 0.8),
        ShapeDef(
          density: 1.0,
          material: SurfaceMaterial(restitution: 0.6),
        ),
      ),
    ],
  );

  @override
  Color get defaultColor => Colors.blue;
}