@echo off
echo ============================================
echo  🌳 Prova 01 - Execucao completa do projeto
echo ============================================

echo Ativando ambiente virtual...
call .venv\Scripts\activate

echo Instalando dependencias...
pip install -r requirements.txt

echo Executando experimentos...
python src\experiments.py

echo Gerando graficos e tabelas...
python src\analysis.py

echo ============================================
echo  ✅ Processo concluido! Resultados em /results
echo ============================================
pause
