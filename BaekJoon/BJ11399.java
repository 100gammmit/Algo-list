import java.util.*;
import java.io.*;
public class BJ11399 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		String[] st = bf.readLine().split(" ");
		int[] arr = new int[n];
		for(int i=0; i < n; i++) {
			arr[i] = Integer.parseInt(st[i]);
		}
		Arrays.sort(arr);
		int p=0, ans=0;
		for(int i=0; i < n; i++) {
			p+=arr[i];
			ans+=p;
		}
		System.out.println(ans);
	}
}