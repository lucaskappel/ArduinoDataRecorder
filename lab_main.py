# -*- coding: utf-8 -*-
# imports #####################################################################
import os
import numpy as np
import matplotlib.pyplot as plt
import re

CD = os.getcwd();
if not os.path.exists(CD + '\\pictures'):
    os.makedirs(CD + '\\pictures')
data_path = 'C:\\Users\\Lucas\\Desktop\\School\\S2020\\ME4720\\Custom_Lab\\good data\\'

def main():
    display_string = ["Name", "Duration [s]", "Max Temperature [C]", "Time Constant [s]"]
    results_array = []
    results_array_string = []
    file_array = load_files()
    for file in file_array:
        this_data = ida(file)
        results_array.append(get_duration_max_temp_and_time_constant(this_data[0], this_data[1]))
        results_array_string.append( [file] + [ str(val) for val in results_array[ len( results_array ) - 1] ] )
    results_file = open(data_path + "\\run_results.txt", "w")
    
    results_file.writelines("\t".join(display_string) + "\n")
    for line in results_array_string:
        results_file.writelines("\t".join(line) + "\n")
    results_file.close()
    pass



##############################################################################
    
def get_duration_max_temp_and_time_constant(time_array, data_array):
    initial_temperature = data_array[0]
    max_temperature = max(data_array)
    temperature_difference = max_temperature - initial_temperature
    time_constant_threshold_temperature = initial_temperature + temperature_difference*0.632
    for i in range(0, len(data_array)):
        if data_array[i] >time_constant_threshold_temperature:
            return [time_array[-1]/2, max_temperature, time_array[i]]
    return [time_array[-1]/2, max_temperature, time_array[0]]

def load_files():
    file_list = []
    for root, dirs, files in os.walk(CD):
            for file in files:
                if file[-4:] == ".txt" and file[:4] == "2020":
                    file_list = file_list + [file]
    return file_list

def ida(file_name):
    for root, dirs, files in os.walk(CD):
        for file in files:
            if re.match(file_name, file):
                return np.transpose(np.loadtxt(data_path + file, skiprows=1 ))
    return

def fit_data(x_data, x_label, y_data, y_label, title_label, legend_label):
    # Linear fit
    coeffs = np.polyfit(x_data, y_data, 1)
    y_fit_data = [(x*coeffs[0] + coeffs[1]) for x in x_data]
    
    # Plotting
    plt.figure()
    ax = plt.subplot(111)
    ax.plot(x_data, y_data, 'ro', markersize=5, label=legend_label)
    ax.plot(x_data, y_fit_data, 'b--', marker='+', markersize=5, label='fit, y = (' + str(np.round(coeffs[0], 3)) + ') x + (' + str(np.round(coeffs[1], 3)) + ')')
    
    # Post-plotting
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title_label)
    ax.legend()
    plt.savefig(CD + '\\pictures\\' + title_label + '.png', dpi=500)
    return

def plot_save(x_data, x_label, y_data, y_label, linespec, legend_label, title_label):
    ax = plt.subplot(111)
    plt.plot(x_data, y_data, linespec, label=legend_label, markersize=4)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    ax.legend()
    return
##############################################################################

if __name__ == "__main__":
    main()






