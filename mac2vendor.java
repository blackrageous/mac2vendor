import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class VendorLookup {

    public static void main(String[] args) throws IOException {

        // Set the input and vendor files
        String input_file = "input.txt";
        String vendor_file = "vendor.txt";

        // Read the vendor file into a map
        Map<String, String> vendorMap = new HashMap<>();
        BufferedReader vendorReader = new BufferedReader(new FileReader(vendor_file));
        String vendorLine = vendorReader.readLine();
        while (vendorLine != null) {
            String[] fields = vendorLine.trim().split("\\s+");
            vendorMap.put(fields[0], fields[1]);
            vendorLine = vendorReader.readLine();
        }
        vendorReader.close();

        // Loop through each line in the input file
        BufferedReader inputReader = new BufferedReader(new FileReader(input_file));
        String inputLine = inputReader.readLine();
        while (inputLine != null) {
            // Extract the hostname, IP, and MAC address from the input line
            String[] fields = inputLine.trim().split("\\s+");
            String hostname = fields[0];
            String ip = fields[1];
            String mac = fields[2];

            // Parse the MAC address to extract the first 6 octets
            String macPrefix = mac.replaceAll(":", "").substring(0, 12);

            // Search the vendor map for the MAC address prefix
            String vendor = vendorMap.getOrDefault(macPrefix, "Unknown");

            // Print the results
            System.out.println("Hostname: " + hostname);
            System.out.println("IP Address: " + ip);
            System.out.println("MAC Address: " + mac);
            System.out.println("Vendor: " + vendor);
            System.out.println();

            inputLine = inputReader.readLine();
        }
        inputReader.close();
    }
}
