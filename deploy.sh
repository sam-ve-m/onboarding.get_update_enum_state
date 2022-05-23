echo "DEPLOYING FISSION FUNCTION..."
source set_variables.sh
echo "RODANDO ARQUIVO configure.sh"; bash configure.sh || { echo "ERROR: Error while running configure.sh [EXITING SCRIPT]"; exit; }
echo "RODANDO ARQUIVO run.sh"; bash run.sh || { echo "ERROR: Error while running run.sh [EXITING SCRIPT]"; exit; }
echo "FISSION DEPLOYED SUCCESSFULLY!"
