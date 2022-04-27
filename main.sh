cp checkpoints/testingRuns/latest_net_G_A.pth ./checkpoints/testingRuns/latest_net_G.pth
python test.py --dataroot datasets/testingRuns/testA --name checkpoints/testingRuns --model test --gpu_ids '-1' --no_dropout
