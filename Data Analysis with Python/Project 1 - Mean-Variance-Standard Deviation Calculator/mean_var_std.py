import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix_np = np.array(list).reshape(3, 3)
    axis1 = [matrix_np[:, 0], matrix_np[:, 1], matrix_np[:, 2]]
    axis2 = [matrix_np[0, :], matrix_np[1, :], matrix_np[2, :]]
    
    mean = [
        [float(np.mean(axis1[0])), float(np.mean(axis1[1])), float(np.mean(axis1[2]))],
        [float(np.mean(axis2[0])), float(np.mean(axis2[1])), float(np.mean(axis2[2]))],
        float(np.mean(matrix_np))
        ]
    variance = [
        [float(np.var(axis1[0])), float(np.var(axis1[1])), float(np.var(axis1[2]))], 
        [float(np.var(axis2[0])), float(np.var(axis2[1])), float(np.var(axis2[2]))],
        float(np.var(matrix_np))
        ]
    std_dev = [
        [float(np.std(axis1[0])), float(np.std(axis1[1])), float(np.std(axis1[2]))], 
        [float(np.std(axis2[0])), float(np.std(axis2[1])), float(np.std(axis2[2]))],
        float(np.std(matrix_np))
        ]
    max = [
        [int(np.max(axis1[0])), int(np.max(axis1[1])), int(np.max(axis1[2]))],
        [int(np.max(axis2[0])), int(np.max(axis2[1])), int(np.max(axis2[2]))],
        int(np.max(matrix_np))
        ]
    min = [
        [int(np.min(axis1[0])), int(np.min(axis1[1])), int(np.min(axis1[2]))], 
        [int(np.min(axis2[0])), int(np.min(axis2[1])), int(np.min(axis2[2]))],
        int(np.min(matrix_np))
        ]
    sum = [
        [int(np.sum(axis1[0])), int(np.sum(axis1[1])), int(np.sum(axis1[2]))], 
        [int(np.sum(axis2[0])), int(np.sum(axis2[1])), int(np.sum(axis2[2]))],
        int(np.sum(matrix_np))
        ]

    calculations = {
        "mean": mean,
        "variance": variance,
        "standard deviation": std_dev,
        "max": max,
        "min": min,
        "sum": sum
    }

    return calculations
