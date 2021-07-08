* Must have Python and virtualenv installed already *

FOR WINDOWS - Command Prompt CLI

Installation Steps:
    1: cd into_desired_folder
    2: git clone https://github.com/SirGlory/arb_ws.git    "from within the created folder"
    3: cd arb_ws                                           "enter project folder"
    4: python -m virtualenv venv                           "Create virtual environment"
    5: .\venv\Scripts\activate                             "Activate virtual environment"
    6: pip install -r requirements.txt                     "Install required packages"


Run Steps:
    For VALR Orderbook:
        python valr_ws.py                       "From within arb_ws folder, run script"

    For Luno Orderbook:
        python luno_ws.py                       "From within arb_ws folder, run script"
                                                "Open second command prompt to run concurrently"