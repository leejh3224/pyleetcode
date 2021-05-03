
# 1472. Design Browser History
# Difficulty: Medium
# Time Complexity: O(1) for every methods in class
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.N = 1
        self.pt = 0

    # It took a while to understand 'visit' operation
    # The description says "Visits url from the current page. It clears up all the forward history."
    # And I couldn't understand the "clears up all the forward history" part and submitted wrong answer
    # What it actually means is that items behind current position should be dropped
    def visit(self, url: str) -> None:
        self.history = self.history[:self.pt+1] + [url]
        self.N = len(self.history)
        self.pt = self.N-1

    def back(self, steps: int) -> str:
        self.pt = max(self.pt - steps, 0)
        return self.history[self.pt]

    def forward(self, steps: int) -> str:
        self.pt = min(self.pt + steps, self.N-1)
        return self.history[self.pt]

