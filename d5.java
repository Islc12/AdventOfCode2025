import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class d5 {
    public static void main(String[] args) {
        File id_ranges = new File("d5_range.txt");
        File ids = new File("d5_ids.txt");
        int fresh = 0;

        try (Scanner idScanner = new Scanner(ids)) {
            while(idScanner.hasNextLong()) {
                long id = idScanner.nextLong();
                try (Scanner scnr = new Scanner(id_ranges)) {
                    while(scnr.hasNextLine()) {
                        String id_range = scnr.nextLine();
                        String[] ranges = id_range.split("-");
                        long start = Long.parseLong(ranges[0].strip());
                        long end = Long.parseLong(ranges[1].strip());
                        if (id >= start && id <= end) {
                            fresh++;
                            break;
                        }
                    }
                }
                catch (FileNotFoundException e) {
                    e.printStackTrace();
                }
            }

        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println(fresh);
    }
}
