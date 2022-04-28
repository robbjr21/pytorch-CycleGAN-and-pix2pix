cp checkpoints/checkpoints/mediumReal/latest_net_G_A.pth checkpoints/checkpoints/mediumReal/latest_net_G.pth
python test.py --dataroot datasets/testingRuns/testA --name checkpoints/mediumReal --model test --gpu_ids '-1' --no_dropout
