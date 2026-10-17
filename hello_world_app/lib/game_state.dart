import 'package:flutter/foundation.dart';

class GameState extends ChangeNotifier {
  double money = 100.0;
  double multiplier = 1.0;
  
  // 4x3 mriežka pre predmety (null = prázdne políčko)
  List<Map<String, dynamic>?> grid = List.filled(12, null);

  void addMoney(double amount) {
    money += amount * multiplier;
    notifyListeners();
  }

  bool buyItem(String type, double cost) {
    if (money >= cost) {
      money -= cost;
      // Nájdeme prázdne miesto v mriežke
      int emptyIndex = grid.indexWhere((item) => item == null);
      if (emptyIndex != -1) {
        grid[emptyIndex] = {"type": type, "level": 1};
        notifyListeners();
        return true;
      }
    }
    return false;
  }

  void mergeItems(int fromIndex, int toIndex) {
    if (grid[fromIndex] != null && grid[toIndex] != null) {
      var item1 = grid[fromIndex]!;
      var item2 = grid[toIndex]!;
      if (item1['type'] == item2['type'] && item1['level'] == item2['level']) {
        grid[toIndex] = {"type": item1['type'], "level": item1['level'] + 1};
        grid[fromIndex] = null;
        notifyListeners();
      }
    } else if (grid[fromIndex] != null && grid[toIndex] == null) {
      grid[toIndex] = grid[fromIndex];
      grid[fromIndex] = null;
      notifyListeners();
    }
  }
}