import sys
import tensorflow as tf
from pathlib import Path


def export_model(h5_path, export_dir):
    model = tf.keras.models.load_model(h5_path, compile=False)
    tf.saved_model.save(model, export_dir)
    print(f"Exported SavedModel in {export_dir}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export_savedmodel.py <path_to_model.h5> <output_dir>")
        sys.exit(1)
    h5_path = sys.argv[1]
    export_dir = sys.argv[2]
    assert Path(h5_path).exists(), f"File {h5_path} does not exist."
    export_model(h5_path, export_dir)
