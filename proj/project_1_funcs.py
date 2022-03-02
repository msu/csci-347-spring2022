import numpy as np

def multivar_mean(D):
	# find the number of rows and columns in input
	n_row = D.shape[0]
	n_col = D.shape[1]

	# initialize an empty numpy array with appropriate number of entries	
	multivariate_mean = np.empty(n_col)

	# find the multivariate mean, by iterating through
	#	each row of each column, summing entries, 
	#	and then dividing by the number of rows
	for j in range(n_col):
		sum_col_j = 0
		for i in range(n_row):
			sum_col_j += D[i][j];
		mean_col_j = sum_col_j/n_row;
		multivariate_mean[j] = mean_col_j;
	
	return multivariate_mean;

def sample_covariance(a,b):
	# find the dimensionality of a and b
	dim = np.shape(a)[0]
	
	# if the arrays don't have the same size, return a NaN
	if(dim != np.shape(b)[0]):
		print('dimensions of inputs do not match');
		return np.nan;
	
	# compute the sample covariance
	mean_a = np.mean(a);
	mean_b = np.mean(b);
	
	# initialize sum of products
	sp = 0;
	
	# sum up squared values 
	for i in range(dim):
		sp += (a[i] - mean_a)*(b[i] - mean_b);

	# divide by dim-1 to get the sample covariance
	sample_cov = sp/(dim-1);
	
	return sample_cov;

# sample correlation coefficient between two numpy vectors
def s_correlation(a,b):
	covariance = sample_covariance(a,b);
	std_a = np.var(a,ddof=1);
	std_b = np.var(b,ddof=1);
	corr = covariance/(std_a*std_b);
	return corr;

def range_normalize(D):
	n_col = D.shape[1];
	range_normalized_D = np.zeros(D.shape);
	for j in range(n_col):
		max_j = max(D[:,j]);
		min_j = min(D[:,j]);
		range_j = max_j - min_j;
		range_normalized_D[:,j] = (D[:,j] - min_j)/range_j;
	return range_normalized_D;

def standard_normalize(D):
	n_col = D.shape[1];
	n_row = D.shape[0];
	standard_normalized_D = np.zeros(D.shape);
	for j in range(n_col):
		mean_j = np.mean(D[:,j]);
		sd_j = np.sqrt(sample_covariance(D[:,j], D[:,j]));
		for i in range(n_row):
			standard_normalized_D[i,j] = (D[i,j] - mean_j)/sd_j;
	return standard_normalized_D;

def covariance_matrix(D):
	n_col = D.shape[1]
	cov_mtx = np.zeros([n_col, n_col]);
	for i in range(n_col):
		for j in range(n_col):
			cov_mtx[i,j] = sample_covariance(D[:,i],D[:,j])
	return cov_mtx; 

def label_encode(D):
	n_row = D.shape[0];
	n_col = D.shape[1];
	label_encoded_D = np.zeros([n_row, n_col])

	for j in range(n_col):
		unique_j, indices = np.unique(D[:,j], return_index=True);
		for i in range(n_row):
			label_encoded_D[i,j] = np.where(unique_j == D[i,j])[0]	

	return label_encoded_D;

# test cases
D = np.array([[0.2, 23, 5.7], [0.4, 1, 5.4], [1.8, 0.5, 5.2], [5.6, 50, 5.1], [-0.5, 34, 5.3], [0.4, 19, 5.4], [1.1, 11, 5.5]])

categorical_D = np.array([['A','L'],['B','S'],['C','S'],['B','L'],['A','M'],['D','S']])

print('D = \n',D)

print('mean of D: ', multivar_mean(D))

def test_multivar_mean():
	eps = 0.00001
	assert (multivar_mean(D).all - np.mean(D, axis=0).all) < eps, "numpy mean should match"

print('covariance of D[:,0] and D[:,1]: ', sample_covariance(D[:,0], D[:,1]));
print('correlation of D[:,0] and D[:,1]: ', s_correlation(D[:,0],D[:,1]))
print('range normalization of D: \n', range_normalize(D))
print('standard normalization of D: \n', standard_normalize(D))
print('covariance matrix of D: \n', covariance_matrix(D))

print('categorical D = \n', categorical_D)
print('label encoding of categorical_D: \n', label_encode(categorical_D))

