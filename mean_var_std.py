import numpy as np

def calculate(list):
    try:
        calculations = {}
        
        calc = np.array(list, dtype=int)
        calc = calc.reshape(3,3)
        
        #mean calculations
        y_axis_mean = (calc.mean(axis=0)).tolist()
        x_axis_mean = (calc.mean(axis=1)).tolist()
        overall_mean = calc.mean()
        calculations['mean'] = [y_axis_mean, x_axis_mean, overall_mean]
        
        #variance calculations
        y_axis_var = (calc.var(axis=0)).tolist()
        x_axis_var = (calc.var(axis=1)).tolist()
        overall_var = calc.var()
        calculations['variance'] = [y_axis_var, x_axis_var, overall_var]
        
        #standard deviation calculations
        y_axis_sd = (calc.std(axis=0)).tolist()
        x_axis_sd = (calc.std(axis=1)).tolist()
        overall_sd = calc.std()
        calculations['standard deviation'] = [y_axis_sd, x_axis_sd, overall_sd]

        #max calculations
        y_axis_max = (calc.max(axis=0)).tolist()
        x_axis_max = (calc.max(axis=1)).tolist()
        overall_max = calc.max()
        calculations['max'] = [y_axis_max, x_axis_max, overall_max]

        #min calculations
        y_axis_min = (calc.min(axis=0)).tolist()
        x_axis_min = (calc.min(axis=1)).tolist()
        overall_min = calc.min()
        calculations['min'] = [y_axis_min, x_axis_min, overall_min]

        #sum calculations
        y_axis_sum = (calc.sum(axis=0)).tolist()
        x_axis_sum = (calc.sum(axis=1)).tolist()
        overall_sum = calc.sum()
        calculations['sum'] = [y_axis_sum, x_axis_sum, overall_sum]

        
        return calculations
    except ValueError:
        raise ValueError("List must contain nine numbers.")




