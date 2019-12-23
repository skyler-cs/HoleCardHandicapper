import os
import csv
from holecardhandicapper.model.const import PREFLOP, FLOP, TURN, RIVER

class Utils:

  @classmethod
  def build_preflop_winrate_table(self):
    fpath = self.get_preflop_winrate_data_path()
    table = [[0 for j in range(53)] for i in range(53)]
    with open(fpath, "r") as f:
      reader = csv.reader(f)
      data = []
      for id1, id2, win_rate in reader:
        id1, id2 = map(int, [id1, id2])
        win_rate = float(win_rate)
        table[id1][id2] = win_rate
    return table

  @classmethod
  def get_preflop_winrate_data_path(self):
    root = self.__get_root_path()
    return os.path.join(root, "holecardhandicapper", "model", "data", "preflop_winrate.csv")


  @classmethod
  def get_model_weights_path(self, street):
    if PREFLOP == street:
      return self.get_preflop_model_weights_path()
    if FLOP == street:
      return self.get_flop_model_weights_path()
    if TURN == street:
      return self.get_turn_model_weights_path()
    if RIVER == street:
      return self.get_river_model_weights_path()
    raise ValueError("Unknown street [ %s ] received." % street)


  @classmethod
  def get_preflop_model_weights_path(self):
    root = self.__get_root_path()
    return os.path.join(root, "holecardhandicapper", "model", "weights", "preflop_neuralnet_model_weights.h5")

  @classmethod
  def get_flop_model_weights_path(self):
    root = self.__get_root_path()
    return os.path.join(root, "holecardhandicapper", "model", "weights", "flop_cnn_model_weights.h5")

  @classmethod
  def get_turn_model_weights_path(self):
    root = self.__get_root_path()
    return os.path.join(root, "holecardhandicapper", "model", "weights", "turn_cnn_model_weights.h5")

  @classmethod
  def get_river_model_weights_path(self):
    root = self.__get_root_path()
    return os.path.join(root, "holecardhandicapper", "model", "weights", "river_cnn_model_weights.h5")

  @classmethod
  def __get_root_path(self):
    return os.path.join(os.path.dirname(__file__), "..", "..")

