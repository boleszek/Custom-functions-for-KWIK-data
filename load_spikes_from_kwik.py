def load_spikes_from_kwik(dfile, clust_choice):
    '''
    This function extracts spike times and cluster labels from the kwik file. Since some
    clusters are unwanted (i.e. noise clusters), the function allows you to choose which
    clusters to load.
    
    Inputs : dfile        - file directory (including filename)
             clust_choice - list of cluster labels you want to extract
        
    Outputs: SPK          - list of spike times for each cluster
    '''
    import h5py
    with h5py.File(dfile,'r') as D:
        # for viewing contents of folders
        # dv=D1['/channel_groups/0/spikes/time_samples']
        # for i in iter(dv):
            # print(i)
        time_samples = D.get('/channel_groups/0/spikes/time_samples')
        np_time_samples = np.array(time_samples)
        cluster_labels = D.get('/channel_groups/0/spikes/clusters/main')
        np_cluster_labels = np.array(cluster_labels)
        
    SPK = []
    for i in range(len(clust_choice)):
        temp_ind = np.squeeze(np.array(np.where(np_cluster_labels == clust_choice[i])))
        SPK.append(np_time_samples[temp_ind])
    return SPK
