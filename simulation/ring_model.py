class Inverter:
    def __init__(self, delay):
        self.delay = delay
        self.timer = 0
        self.state = 0

    def update(self, input_signal):
        if self.timer <= 0:
            self.state = 1 - input_signal
            self.timer = self.delay
        else:
            self.timer -= 1
        return self.state


class RingCounter:
    def __init__(self, delays):
        self.nodes = [Inverter(d) for d in delays]

    def step(self, input_signal):
        signals = [input_signal]

        for node in self.nodes:
            signals.append(node.update(signals[-1]))

        return signals[1:]


if __name__ == "__main__":
    ring = RingCounter([2, 3, 2, 4, 3])

    signal = 1
    for i in range(20):
        output = ring.step(signal)
        print(output)
        signal = output[-1]
