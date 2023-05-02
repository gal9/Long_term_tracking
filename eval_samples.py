from eval_tracker import evaluate_tracker

samples = [1, 3, 5, 10, 20, 50]

for sample_n in samples:
    res_name = "./results/samples_" + str(sample_n)
    print(res_name, flush=True)

    evaluate_tracker("./data", "models/siamfc_net.pth", res_name, visualize=False, search_num=sample_n)