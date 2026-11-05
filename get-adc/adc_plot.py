import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.title("Зависимость напряжения от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.xlim(0, max(time) if time else 1)
    plt.ylim(0, max_voltage)
    plt.grid(True)
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []
    for i in range(len(time) - 1):
        sampling_periods.append(time[i + 1] - time[i])
    
    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods, bins=50)
    plt.title("Распределение количества сделанных измерений по их продолжительности")
    plt.xlabel("Продолжительность измерения, с")
    plt.ylabel("Количество измерений")
    plt.xlim(0, 0.002)
    plt.grid(True)
    plt.show()
