import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws Exception {

        String inputPath = "./input";
        List<Integer> tabA = new ArrayList<>();
        List<Integer> tabB = new ArrayList<>();

        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(inputPath))) {
            bufferedReader.lines()
                    .map(line -> line.trim().split("\\s+"))
                    .forEach(parts -> {
                        tabA.add(Integer.parseInt(parts[0]));
                        tabB.add(Integer.parseInt(parts[1]));
                    });
        }

        Collections.sort(tabA);
        Collections.sort(tabB);

        int resultP1 = IntStream.range(0, tabA.size())
            .map(i -> Math.abs(tabA.get(i) - tabB.get(i)))
            .sum();

        System.out.println(resultP1);

        int reusltP2 = tabA.stream()
            .mapToInt(val -> val * Collections.frequency(tabB, val))
            .sum();

        System.out.println(reusltP2);
    }
}
