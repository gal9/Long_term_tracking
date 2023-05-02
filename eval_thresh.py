from eval_tracker import evaluate_tracker

threshold_factors = [0.4, 0.5, 0.55, 0.6, 0.65, 0.7]

for threshold_factor in threshold_factors:
    res_name = "./results/threshold_0" + str(threshold_factor)[2:]
    print(threshold_factor, flush=True)

    evaluate_tracker("./data", "models/siamfc_net.pth", res_name, visualize=False, threshold_factor=threshold_factor)