import datetime
import Preprocessing
import sys

#Read in the metadata file
metadata_file = sys.argv[1]
metadata = Preprocessing.Read_Metadata_File(metadata_file)
ncores = metadata['parallel_ncores']

#Define the dates
idate = datetime.datetime(metadata['startdate']['year'],
			   metadata['startdate']['month'],
			   metadata['startdate']['day'],0)
fdate = datetime.datetime(metadata['enddate']['year'],
			   metadata['enddate']['month'],
			   metadata['enddate']['day'],23)

#Define the info
hydrobloks_info = {
        'icatch':metadata['catchment_id'],
	'input_file':metadata['input_file'],
	'output_file':metadata['output_file'],
        #'soil_file':metadata['soil_file'],
        'workspace':metadata['workspace'],
	'surface_flow_flag':metadata['surface_flow_flag'],
	'subsurface_flow_flag':metadata['subsurface_flow_flag'],
	'dt':metadata['dt'],#seconds
	'dtt':metadata['dtt'],#seconds
	'dx':metadata['dx'],#meters
	'nsoil':metadata['nsoil'],
	'ncores':metadata['parallel_ncores'],
	'idate':idate,
	'fdate':fdate,
	'nclusters_nc':metadata['nhru_nc'],
	'nclusters_c':metadata['nhru_c'],
	'nclusters':metadata['nhru_nc'] + metadata['nhru_c'],
	'model_type':metadata['model_type'],
        'create_mask_flag':metadata['create_mask_flag'],
        'covariates':metadata['covariates'],
        'clustering_type':metadata['clustering_type'],
        'hillslope_info':metadata['hillslope_info'],
        'basin_info':metadata['basin_info'],
	}

#Cluster the data
Preprocessing.Prepare_Model_Input_Data(hydrobloks_info)
