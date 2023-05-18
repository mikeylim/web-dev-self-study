import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int numOfTests = Integer.parseInt(br.readLine());
            
            for (int i = 0; i < numOfTests; i++) {
                String inputString = br.readLine();
                String[] inputList = inputString.split(" ");
                bw.write(Integer.parseInt(inputList[0]) + Integer.parseInt(inputList[1]) + "\n");
            }
            bw.flush();
            bw.close();
        } catch (Exception e) {
            // handle exception
            e.printStackTrace();
        }
    }
}