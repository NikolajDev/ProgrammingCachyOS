import 'package:flame/events.dart';
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
            do: GameWidget(game: PlinkoWorld(gameState)),
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
                          onAccept: (fromIndex) {
                            gameState.mergeItems(fromIndex, index);
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
  PlinkoWorld(this.gameState) : super(zoom: 20);

  @override
  Future<void> onLoad() async {
    await super.onLoad();
    // Pridanie gravitácie a základných objektov / prekážok
    add(Ball(Vector2(0, -15), gameState));
  }
}

class Ball extends BodyComponent {
  final GameState gameState;
  Ball(Vector2 position, this.gameState) : super();

  @override
  Body createBody() {
    final bodyDef = BodyDef(
      type: BodyType.dynamic,
      position: position,
    );
    final shape = CircleShape()..radius = 0.8;
    final fixtureDef = FixtureDef(shape)
      ..density = 1.0
      ..restitution = 0.6;
    return world.createBody(bodyDef)..createFixture(fixtureDef);
  }
}