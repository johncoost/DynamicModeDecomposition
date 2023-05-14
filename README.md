# DynamicModeDecomposition
Dynamic Mode Decomposition is class of algorithms used to identify spatio-temporal coherent patterns in high-dimensional data.

The first algorithm we exploit is the Hankel DMD. We start by creating a hankel matrix of time series values and perform SVD to this matrix. SVD enables to find the most important spatiotemporal coherent patterns and therefore, we can reconstuct the time series in order to obtain a prediction which better approximate it.
