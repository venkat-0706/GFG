class Solution {
	public:
	int sameMod(vector<int> &arr) {
		// code here
		int n = arr.size();
		int result = 0;
		int k = 1;
		bool allEqual = true;
		for (int i = 0; i<n; ++i) {
			k = max(arr[i], k);
			if (i>0 && arr[i] != arr[i - 1])allEqual = false;
		}
		if (allEqual)return - 1;
		for (int i = 1; i <= k; ++i) {
			int prevRemainder = -1;
			bool equalRemainder = true;
			for (int j = 0; j<n; ++j) {
				int remainders = arr[j]%i;
				if (prevRemainder == -1)prevRemainder = remainders;
				else {
					if (prevRemainder != remainders) {
						equalRemainder = false;
						break;
					}
				}
			}
			if (equalRemainder)result++;
		}
		return result;
	}
};