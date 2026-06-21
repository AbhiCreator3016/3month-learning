
import json
# ── BASIC TRY/EXCEPT ─────────────────────────────────────────────
# print("This specific file teaches you error handling:")

# def predict_placement(cgpa, problems):
#     try:
#         score = cgpa/problems
#         return score
#     except ZeroDivisionError:
#         print("Warning problem solved cannot be zero!!!")
#         return None


# print(predict_placement(8.0, 50))   
# print(predict_placement(8.0, 0))

# ── CATCHING MULTIPLE EXCEPTION TYPES ─────────────────────────────
# def load_model_config(filepath):
#     try:
#         with open(filepath,"r") as file:
#             config = json.load(file)
#         return config
#     except FileNotFoundError:
#         print(f"Error: '{filepath}' not found/ does not exist.")
#         return{}
#     except json.JSONDecodeError:
#         print(f"Error: '{filepath}' does not exist.")
#         return {}
#     except Exception as e:
#         print(f"Unexpected error: {e}.")
#         return {}

# load_model_config("")

# ── ELSE AND FINALLY ─────────────────────────────────────────────
# def safe_divide(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print(f"Cannot divide by zero !!!")
#         return None
#     else:
#         print("Divison successful")
#         return result
#     finally:
#         print(f"Operation Complete.")


# safe_divide(10, 2)
# print("---")
# safe_divide(10, 0)

# ── CUSTOM EXCEPTION ─────────────────────────────────────────────
# Create our own exception type by inheriting from Exception
class ModelNotTrainedError(Exception):
    pass


class Model:
    def __init__(self):
        # Object starts in "not trained" state
        self.is_trained = False

    def predict(self, x):
        # Step 1: Validate prerequisite
        if not self.is_trained:

            # Step 2: Create and THROW an exception object
            # Execution STOPS here inside predict()
            # return x * 2 will NEVER run
            raise ModelNotTrainedError(
                "Call train() before predict()"
            )

        # Runs only if no exception was raised
        return x * 2


# Step 3: Create object
m = Model()

try:
    # Step 4: Execute risky code
    # Python enters predict()
    m.predict(5)

# Step 5: If ANY Exception-derived error occurs,
# Python jumps here immediately
except Exception as e:

    # 'e' stores the actual exception object
    # str(e) -> "Call train() before predict()"
    print(f"Caught: {e}")

# Step 6: Program continues after try-except