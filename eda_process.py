

#%%

import pandas as pd

df_shabina = pd.read_excel('data.xlsx', sheet_name='shabina')
df_roshni = pd.read_excel('data.xlsx', sheet_name='roshni')

#%%

# Load the NeuroKit package and other useful packages
import neurokit2 as nk
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [15, 5]  # Bigger images

array1 = df_roshni.to_numpy() 
time_r =array1[:,0]
eda_r = array1[:,1]

array2 = df_shabina.to_numpy() 
time_s =array2[:,0]
eda_s = array2[:,1]


#%%

signals, info = nk.eda_process(eda_r, sampling_rate=21.74)
# Extract clean EDA and SCR features
cleaned = signals["EDA_Clean"]
features = [info["SCR_Onsets"], info["SCR_Peaks"], info["SCR_Recovery"]]
# Visualize SCR features in cleaned EDA signal
plot = nk.events_plot(features, cleaned, color=['red', 'blue', 'orange'])
# Filter phasic and tonic components
data = nk.eda_phasic(nk.standardize(eda_s), sampling_rate=21.74)
data["EDA_Raw"] = eda_s # Add raw signal
data.plot()
# Plot EDA signal
plot = nk.eda_plot(signals)

#%%

signals, info = nk.eda_process(eda_s, sampling_rate=21.74)
# Extract clean EDA and SCR features
cleaned = signals["EDA_Clean"]
features = [info["SCR_Onsets"], info["SCR_Peaks"], info["SCR_Recovery"]]
# Visualize SCR features in cleaned EDA signal
plot = nk.events_plot(features, cleaned, color=['red', 'blue', 'orange'])
# Filter phasic and tonic components
data = nk.eda_phasic(nk.standardize(eda_s), sampling_rate=21.74)
data["EDA_Raw"] = eda_s # Add raw signal
data.plot()
# Plot EDA signal
plot = nk.eda_plot(signals)

#%%



