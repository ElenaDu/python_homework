#Task 5: Extending a Class
import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        total_rows = len(self)
        for i in range(0, total_rows, 10):
            print("\n" + "+" + "-" * 45 + "+")
            print(f"Rows {i} to {min(i+9, total_rows-1)}")
            print(super().iloc[i:i+10])

# Main execution block
if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")
    dfp.print_with_headers()
