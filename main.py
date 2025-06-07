import re
import matplotlib.pyplot as plt

log_file = "logs_D/log.txt"

epochs = []
losses = []
accuracies = []

# 正则提取 epoch、loss、test acc
pattern = re.compile(r"Epoch (\d+), Avg Loss: ([\d\.]+), Test Acc: ([\d\.]+)%")

with open(log_file, "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            epoch = int(match.group(1))
            loss = float(match.group(2))
            acc = float(match.group(3))
            epochs.append(epoch)
            losses.append(loss)
            accuracies.append(acc)

# 绘图
plt.figure(figsize=(12, 5))

# 子图 1：Loss 曲线
plt.subplot(1, 2, 1)
plt.plot(epochs, losses, color='red', linewidth=2, marker='o', label="Avg Loss")
plt.xlabel("Epoch", fontsize=12)
plt.ylabel("Loss", fontsize=12)
plt.title("Loss vs. Epoch", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=10)

# 子图 2：Accuracy 曲线
plt.subplot(1, 2, 2)
plt.plot(epochs, accuracies, color='orange', linewidth=2, marker='o', label="Test Accuracy (%)")
plt.xlabel("Epoch", fontsize=12)
plt.ylabel("Accuracy (%)", fontsize=12)
plt.title("Accuracy vs. Epoch", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=10)

plt.tight_layout()
plt.savefig("logs_D/training_result.png", dpi=300)
plt.show()
