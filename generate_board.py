#python3

from absl import app
from absl import flags
from typing import Sequence, Text

FLAGS = flags.FLAGS

flags.DEFINE_string("email1", None, "for example, 'his-email@example.com'")
flags.DEFINE_string("email2", None, "for example, 'her-email@example.com'")

flags.mark_flag_as_required("email1")
flags.mark_flag_as_required("email2")


def generate_board() -> None:
	

def main(argv: Sequence[Text]) -> None:
  """Program to generate a secret code card for Codenames Duet.

  Args:
    argv: Not used
  Returns:
    None on no error, non-None on error.
  """


  print("TODO")


if __name__ == "__main__":
  app.run(main)
