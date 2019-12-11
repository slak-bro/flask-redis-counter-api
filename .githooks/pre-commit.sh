#!/bin/sh
set -e

echo "\e[1m\e[4mPre-commit hook\e[0m"
echo "\e[4mFormat checking ...\e[0m";
pipenv run black --diff --check ./ || (echo "\e[91mFormatter error, please format using \e[4mpipenv run format\e[0m"; false)
pipenv run isort --diff --check || (echo "\e[91mImport order error, please format using \e[4mpipenv run format\e[0m"; false)
echo "\e[4mLint checking ...\e[0m";
pipenv run lint || (echo "\e[91mLinter error"; false)

echo "\e[1m\e[4m\e[92mPre-commit hook success\e[0m"