import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int t = Integer.parseInt(line.trim());
        
        while (t-- > 0) {
            String[] firstLine = br.readLine().trim().split("\\s+");
            int n = Integer.parseInt(firstLine[0]);
            long x = Long.parseLong(firstLine[1]);
            long y = Long.parseLong(firstLine[2]);
            
            String s = br.readLine().trim();
            
            String[] pLine = br.readLine().trim().split("\\s+");
            long[] p = new long[n];
            long sumP = 0;
            long minA = 0;
            long minB = 0;
            
            for (int i = 0; i < n; i++) {
                p[i] = Long.parseLong(pLine[i]);
                sumP += p[i];
                if (s.charAt(i) == '0') {
                    minA += (p[i] / 2) + 1;
                } else {
                    minB += (p[i] / 2) + 1;
                }
            }
            
            if (x + y < sumP || x < minA || y < minB) {
                System.out.println("NO");
                continue;
            }

            long totalVoters = x + y;
            long maxA = 0;
            long maxB = 0;

            for (int i = 0; i < n; i++) {
                if (s.charAt(i) == '0') {
                    maxA += totalVoters;
                    maxB += (p[i] - 1) / 2;
                } else {
                    maxB += totalVoters;
                    maxA += (p[i] - 1) / 2;
                }
            }

            

            long extraNeeded = totalVoters - sumP;
            
            if (x <= maxA && y <= maxB) {
                long marginA = 0;
                long marginB = 0;
                
                for(int i = 0; i < n; i++) {
                    if (s.charAt(i) == '0') {
                        marginA += ( (p[i] % 2 == 0) ? 1 : 1 ); 
                    } else {
                        marginB += ( (p[i] % 2 == 0) ? 1 : 1 );
                    }
                }

                if (x > totalVoters - (long)s.replace("0", "").length() || 
                    y > totalVoters - (long)s.replace("1", "").length()) {
                    System.out.println("NO");
                } else {
                    System.out.println("YES");
                }
            } else {
                System.out.println("NO");
            }
        }
    }
}