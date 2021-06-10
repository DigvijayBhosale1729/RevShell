echo "Installing cx_Freeze via pip3"
pip3 install cx_freeze
echo "cx_Freeze installed"
echo "Running setup.py"
python3 setup.py build
echo "executable will be found in the build folder"

