from pandasgui import show
import pickle

filepath = "varsey_pushes_current.pkl"
data_file = open(filepath, "rb")
df_arch = pickle.load(data_file)
data_file.close()

show(df_arch)