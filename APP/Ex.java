import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Ex {
    public static void main(String[] args) {
        // JDBC URL, username, and password of MySQL server
        String url = "jdbc:mysql://localhost:3306/Parking";
        String user = "root";
        String password = "1234";

        try {
            // Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            // Open a connection
            Connection connection = DriverManager.getConnection(url, user, password);

            if (connection != null) {
                System.out.println("Connected to the database");
                // You can perform database operations here
                // ...

                // Close the connection
                connection.close();
                System.out.println("Connection closed");
            }
        } catch (ClassNotFoundException e) {
            System.out.println("JDBC Driver not found");
            e.printStackTrace();
        } catch (SQLException e) {
            System.out.println("Connection failed");
            e.printStackTrace();
        }
    }
}