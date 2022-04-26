cp /checkpoints/testingRuns/latest_net_G_A.pth /checkpoints/testingRuns/latest_net_G.pth
python test.py --dataroot datasets/testingRuns/testA --name checkpoints/testingRuns --model test --no_dropout --use_wandb
