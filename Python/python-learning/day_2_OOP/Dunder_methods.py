class TrainingHistory:
    """
    Stores loss and accuracy per epoch.
    We'll make it behave like a Python list.
    """
    def __init__(self):
        self.epochs   = []
        self.losses   = []
        self.accuracies = []

    def add(self, epoch, loss, accuracy):
        self.epochs.append(epoch)
        self.losses.append(loss)
        self.accuracies.append(accuracy)

    # ── DUNDER METHODS ────────────────────────────────────────

    def __len__(self):
        """len(history) → number of epochs recorded."""
        return len(self.epochs)

    def __str__(self):
        """print(history) → human-readable summary."""
        if not self.epochs:
            return "No training history yet."
        return (f"TrainingHistory: {len(self)} epochs | "
                f"Final loss: {self.losses[-1]:.4f} | "
                f"Final accuracy: {self.accuracies[-1]:.2%}")

    def __repr__(self):
        """repr(history) → developer-facing string."""
        return f"TrainingHistory(epochs={len(self)})"

    def __getitem__(self, index):
        """history[i] → get epoch data by index."""
        return {
            "epoch"   : self.epochs[index],
            "loss"    : self.losses[index],
            "accuracy": self.accuracies[index]
        }

    def __contains__(self, epoch_num):
        """5 in history → check if epoch exists."""
        return epoch_num in self.epochs

    def best_epoch(self):
        """Return the epoch with highest accuracy."""
        best_idx = self.accuracies.index(max(self.accuracies))
        return self[best_idx]


# ── USING DUNDER METHODS ──────────────────────────────────────
history = TrainingHistory()
history.add(1,  0.8432, 0.62)
history.add(2,  0.6721, 0.74)
history.add(3,  0.4502, 0.83)
history.add(4,  0.3011, 0.89)
history.add(5,  0.1823, 0.94)

print(history)              # calls __str__
print(len(history))         # calls __len__  → 5
print(history[2])           # calls __getitem__ → epoch 3 data
print(5 in history)         # calls __contains__ → True
print(history.best_epoch()) # → epoch 5