from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    while not anvil.users.login_with_form():
     pass
    
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_1.text
    weight = int(self.text_box_2.text)
    address = self.text_area_1.text
    personal = self.check_box_1.checked
    email = self.text_box_3.text
    anvil.server.call('submit', name=name, weight=weight, address=address, personal=personal, email=email )
    Notification("Your response has been recorded").show()
    print("Welcome to the fitness world!")