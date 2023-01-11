fission spec init
fission env create --spec --name onb-br-enum-state-env --image nexus.sigame.com.br/fission-onboarding-br-enum-state:0.2.0-0 --poolsize 0 --version 3 --imagepullsecret "nexus-v3" --spec
fission fn create --spec --name onb-br-enum-state-fn --env onb-br-enum-state-env --code fission.py --targetcpu 80 --executortype newdeploy --maxscale 3 --requestsperpod 10000 --spec
fission route create --spec --name onb-br-enum-state-rt --method GET --url /enum/state --function onb-br-enum-state-fn
