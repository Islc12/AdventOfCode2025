import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class d4 {
    public static void main(String[] args) {
        File id_ranges = new File("d5_range.txt");
        File ids = new File("d5_ids.txt");
        int fresh = 0;
        List<Long> idArray = new ArrayList<>();
        List<Long> rangeArray = new ArrayList<>();


        try (Scanner idScanner = new Scanner(ids)) {
            while(idScanner.hasNextLong()) {
                idArray.add(idScanner.nextLong());
            }
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        try (Scanner scnr = new Scanner(id_ranges)) {
            for (int i = 0; i < idArray.size(); i++) {
                while(scnr.hasNextLine()) {
                    String id_range = scnr.nextLine();
                    String[] ranges = id_range.split("-");
                    long start = Long.parseLong(ranges[0].strip());
                    long end = Long.parseLong(ranges[1].strip());
                }
            }
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
