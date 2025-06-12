analysis = "AP_Template_R3"
nano_version = 'v12'

#--------------------------------------------------------------------------------------------------
# Production ID:
# 00-09(Data), 10-19(MC-signal), 20-98(MC-bkg), 99(private sample)
#
# Data taking interval (DTI):
# 2022 DTIs = 0(preEE), 1(postEE)
# 2023 DTIs = 0(preBPix), 1(postBPix)
#--------------------------------------------------------------------------------------------------

paths = {}
paths["0_22"] = analysis+'/Datasets/Files/bkg_22/dti_0/'+nano_version+'/'
paths["1_22"] = analysis+'/Datasets/Files/bkg_22/dti_1/'+nano_version+'/'
paths["0_23"] = analysis+'/Datasets/Files/bkg_23/dti_0/'+nano_version+'/'
paths["1_23"] = analysis+'/Datasets/Files/bkg_23/dti_1/'+nano_version+'/'


# https://xsecdb-xsdb-official.app.cern.ch/
b_ds_info = { # [DatasetName, Production ID, PROC_XSEC[pb], XSEC_UNC[pb], XSEC_Accuracy]
"TT": [
    ["TTtoLNu2Q",                       '23',       405.7,              0.1345,		        'NLO'],
    ["TTto2L2Nu",                       '23',       98.04,              0.1345,             'NLO'],
],

"Zto2Nu": [
    ["Zto2Nu_PTNuNu-40to100_1J",        '26',       929.8,	            5.481,		        'LO'],
    ["Zto2Nu_PTNuNu-40to100_2J",        '26',       335.5,	            3.49,		        'LO'],
    ["Zto2Nu_PTNuNu-100to200_1J",       '26',       86.38,	            0.441,		        'LO'],
    ["Zto2Nu_PTNuNu-100to200_2J",       '26',       100.4,	            0.8555,		        'LO'],
    ["Zto2Nu_PTNuNu-200to400_1J",       '26',       6.354,	            0.03067,		    'LO'],
    ["Zto2Nu_PTNuNu-200to400_2J",       '26',       13.86,	            0.09802,		    'LO'],
    ["Zto2Nu_PTNuNu-400to600_1J",       '26',       0.2188,	            0.0009573,		    'LO'],
    ["Zto2Nu_PTNuNu-400to600_2J",       '26',       0.7816,	            0.005088,		    'LO'],
    ["Zto2Nu_PTNuNu-600_1J",            '26',       0.02583,	        0.000108,		    'LO'],
    ["Zto2Nu_PTNuNu-600_2J",            '26',       0.1311,	            0.0007098,		    'LO'],
],
}


#----------------------------------------------------------------------------------------
# [DO NOT TOUCH THIS PART]
#----------------------------------------------------------------------------------------
b_ds = {}
for period in paths.keys():

    dti = period[0]
    year = period[-2:]

    for key in b_ds_info.keys():
        b_ds[key+"_"+period] = []
        for ds in b_ds_info[key]:
            list_temp = []
            list_temp.append(ds[0]+"_"+period)
            list_temp.append(ds[1]+year+dti)
            list_temp.append(paths[period]+ds[0]+".txt")
            list_temp.append(ds[2])
            list_temp.append(ds[3])
            b_ds[key+"_"+period].append(list_temp)

