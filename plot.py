import matplotlib.pyplot as plt
from die_class import Die


class DiceDistributionChart:
    def __init__(self, num_rolls, num_sides):
        self.die_1 = Die(num_sides)
        self.die_2 = Die(num_sides)
        self.fig, self.axes = plt.subplots(1, 2, figsize=(12, 6))
        self.num_rolls = num_rolls

    def _get_values(self):
        self.results_1 = [
            self.die_1.roll()
            for _ in range(self.num_rolls)
        ]
        self.results_2 = [
            self.die_1.roll() + self.die_2.roll()
            for _ in range(self.num_rolls)
        ]

        self.poss_results_1 = range(1, self.die_1.sides+1)
        self.poss_results_2 = range(2, self.die_1.sides + self.die_2.sides+1)

        self.frequencies_1 = [
           self.results_1.count(value)
           for value in self.poss_results_1
        ]
        self.frequencies_2 = [
            self.results_2.count(value)
            for value in self.poss_results_2
        ]

    def _setup_axes(self):
        self.axes[0].bar(self.poss_results_1, self.frequencies_1,
                         color='steelblue', edgecolor='black')
        self.axes[1].bar(self.poss_results_2, self.frequencies_2,
                         color='orange', edgecolor='black')

    def _customize_axes(self):
        self.axes[0].set_title("One D6 Die", fontweight='bold', fontsize=20)
        self.axes[0].set_xlabel("Result", fontsize=14)
        self.axes[0].set_ylabel("Frequency", fontsize=14)
        self.axes[0].set_xticks(self.poss_results_1)
        self.axes[0].tick_params(
            axis="both",
            which="major",
            length=6,
            width=2,
            color="black"
        )

        self.axes[1].set_title("Two D6 Dices", fontweight='bold', fontsize=20)
        self.axes[1].set_xlabel("Sum of Results", fontsize=14)
        self.axes[1].set_ylabel("Frequency", fontsize=14)
        self.axes[1].set_xticks(self.poss_results_2)
        self.axes[1].tick_params(
            axis="both",
            which="major",
            length=6,
            width=2,
            color="black"
        )

    def update(self):
        self.axes[0].clear()
        self.axes[1].clear()

        self._get_values()
        self._setup_axes()
        self._customize_axes()

        self.fig.tight_layout()
        plt.show()


# Input Your Number of rolls and Number of sides
# of the Die and watch the results:
chart_1 = DiceDistributionChart(num_rolls=5000, num_sides=15)
chart_1.update()
