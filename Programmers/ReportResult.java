import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        HashMap<String, Integer> rptm= new HashMap<String, Integer>(id_list.length);
        Map<String, List<String>> myMaps = new HashMap<String, List<String>>(id_list.length);
        for(int i=0; i < id_list.length; i++) {
        	rptm.put(id_list[i], 0);
        	myMaps.put(id_list[i], new ArrayList<String>());
        }
        String[] splrp;
        for(int i=0; i < report.length; i++) {
        	splrp = report[i].split(" ");
        	if(!myMaps.get(splrp[0]).contains(splrp[1])) {
        		myMaps.get(splrp[0]).add(splrp[1]);
        		rptm.put(splrp[1], rptm.get(splrp[1])+1);
        	}   
        }
        for (String i : id_list) {
           if (rptm.get(i) >= k) {
            	for (int j=0; j < id_list.length; j++) {
            		if(myMaps.get(id_list[j]).contains(i)) {
            			answer[j]++;
            		}
            	}
            }
        }
        
        return answer;
    
    }
}