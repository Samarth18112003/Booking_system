
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class appproject {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowNewPage();
            }
        });
    }

    private static void createAndShowNewPage() {
        JFrame frame = new JFrame("New Page");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setUndecorated(true);

        JPanel newPagePanel = new JPanel(new BorderLayout());
        newPagePanel.setBackground(Color.BLACK);

        JPanel headerPanel = new JPanel(new BorderLayout());
        headerPanel.setBackground(Color.DARK_GRAY);
        headerPanel.setPreferredSize(new Dimension(frame.getWidth(), 100));

        JLabel titleLabel = new JLabel("  PARKING");
        titleLabel.setForeground(Color.WHITE);
        titleLabel.setFont(new Font("Times New Roman", Font.PLAIN, 54));
        headerPanel.add(titleLabel, BorderLayout.WEST);

        JButton loginButton = new JButton("Login");
        loginButton.setFont(new Font("Times New Roman", Font.PLAIN, 42));
        loginButton.setForeground(Color.WHITE);
        loginButton.setContentAreaFilled(false);
        loginButton.setBorderPainted(false);
        headerPanel.add(loginButton, BorderLayout.EAST);

        // Create an empty content panel
        JPanel contentPanel = new JPanel();
        contentPanel.setBackground(Color.BLACK);

        // Add the header and content panels to the new page panel
        newPagePanel.add(headerPanel, BorderLayout.NORTH);
        newPagePanel.add(contentPanel, BorderLayout.CENTER);

        loginButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                loginFrame(frame);
            }
        });

        frame.add(newPagePanel);
        frame.setVisible(true);
    }

    private static void loginFrame(JFrame frame_1) {
        // frame_1.dispose();
        JFrame frame2 = new JFrame("Login Screen");
        frame2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame2.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame2.setUndecorated(true);

        JPanel backgroundPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.setColor(Color.BLACK);
                g.fillRect(0, 0, getWidth(), getHeight());
            }
        };
        backgroundPanel.setLayout(new BorderLayout());

        JPanel panel = new JPanel(new GridBagLayout());
        panel.setPreferredSize(new Dimension(350, 390));
        panel.setOpaque(false);
        GridBagConstraints gbc = new GridBagConstraints();

        JLabel label = new JLabel("LOGIN", SwingConstants.CENTER);
        label.setForeground(Color.WHITE);
        label.setFont(new Font("Times New Roman", Font.PLAIN, 74));

        JLabel userLabel = new JLabel("Username:");
        userLabel.setFont(new Font("Times New Roman", Font.PLAIN, 34));
        userLabel.setForeground(Color.WHITE);
        JTextField userField = new JTextField(20);
        userField.setFont(new Font("Times New Roman", Font.PLAIN, 34));

        JLabel passLabel = new JLabel("Password:");
        passLabel.setForeground(Color.WHITE);
        passLabel.setFont(new Font("Times New Roman", Font.PLAIN, 34));
        JPasswordField passField = new JPasswordField(20);
        passField.setFont(new Font("Times New Roman", Font.PLAIN, 34));

        JButton loginButton = new JButton("Login");
        loginButton.setPreferredSize(new Dimension(100, 34));
        loginButton.setFont(new Font("Times New Roman", Font.PLAIN, 24));
        loginButton.setForeground(Color.BLACK);

        JLabel resultLabel = new JLabel("");
        resultLabel.setForeground(Color.RED);

        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 2;
        gbc.insets = new Insets(5, 120, 170, 120);
        panel.add(label, gbc);

        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 1;
        gbc.insets = new Insets(10, 20, 20, 10);
        panel.add(userLabel, gbc);

        gbc.gridx = 1;
        gbc.insets = new Insets(10, 10, 20, 20);
        panel.add(userField, gbc);

        gbc.gridx = 0;
        gbc.gridy = 3;
        gbc.insets = new Insets(10, 20, 30, 10);
        panel.add(passLabel, gbc);

        gbc.gridx = 1;
        gbc.insets = new Insets(10, 10, 30, 20);
        panel.add(passField, gbc);

        gbc.gridx = 0;
        gbc.gridy = 4;
        gbc.gridwidth = 80;
        panel.add(loginButton, gbc);

        gbc.gridy = 5;
        panel.add(resultLabel, gbc);

        backgroundPanel.add(panel);

        loginButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String username = userField.getText();
                String password = new String(passField.getPassword());

                if (username.equals("admin") && password.equals("password")) {
                    resultLabel.setText("Login Successful!");
                    frame_3(frame2);
                } else {
                    resultLabel.setText("Login Failed. Please try again.");
                }
            }
        });

        frame2.add(backgroundPanel);

        frame2.setVisible(true);
    }

    private static void frame_3(JFrame frame_2) {
        // frame_2.dispose();
        JFrame frame3 = new JFrame("Blank Screen");
        frame3.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame3.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame3.setUndecorated(true);

        JPanel blankPanel = new JPanel();
        blankPanel.setBackground(Color.black);

        blankPanel.setLayout(new GridLayout(3, 1));

        JPanel row1 = new JPanel();
        row1.setLayout(new FlowLayout(FlowLayout.CENTER));

        JPanel row2 = new JPanel();
        row2.setLayout(new FlowLayout(FlowLayout.CENTER));

        JPanel row3 = new JPanel();
        row3.setLayout(new FlowLayout(FlowLayout.CENTER));

        ImageIcon im1 = new ImageIcon("C:\\Users\\Admin\\OneDrive\\Desktop\\car.png");
        JButton pr1 = new JButton(im1);
        pr1.setPreferredSize(new Dimension(325, 325));
        pr1.setFont(new Font("Times New Roman", Font.PLAIN, 24));
        ImageIcon im2 = new ImageIcon("C:\\Users\\Admin\\OneDrive\\Desktop\\truck.png");
        JButton pr2 = new JButton(im2);
        pr2.setPreferredSize(new Dimension(325, 325));
        pr2.setFont(new Font("Times New Roman", Font.PLAIN, 24));
        JButton pr3 = new JButton("3");
        pr3.setPreferredSize(new Dimension(325, 325));
        pr3.setFont(new Font("Times New Roman", Font.PLAIN, 24));
        pr3.setForeground(Color.BLACK);
        JButton pr4 = new JButton("4");
        pr4.setPreferredSize(new Dimension(325, 325));
        pr4.setFont(new Font("Times New Roman", Font.PLAIN, 24));
        pr4.setForeground(Color.BLACK);
        JButton pr5 = new JButton();
        pr5.setPreferredSize(new Dimension(325, 325));
        pr5.setFont(new Font("Times New Roman", Font.PLAIN, 24));
        pr5.setForeground(Color.BLACK);
        JButton pr6 = new JButton("6");
        pr6.setPreferredSize(new Dimension(325, 325));
        pr6.setFont(new Font("Times New Roman", Font.PLAIN, 24));
        pr6.setForeground(Color.BLACK);

        row2.add(pr1);
        row2.add(pr2);
        row2.add(pr3);
        row3.add(pr4);
        row3.add(pr5);
        row3.add(pr6);

        pr1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                parkFrame(frame3);
            }
        });

        blankPanel.add(row1);
        blankPanel.add(row2);
        blankPanel.add(row3);

        frame3.add(blankPanel);
        frame3.setVisible(true);
    }

    public static void parkFrame(JFrame frame) {
        JFrame frame4 = new JFrame("pr1");
        frame4.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame4.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame4.setUndecorated(true);

        ImageIcon bg1 = new ImageIcon("C:\\Users\\Admin\\OneDrive\\Desktop\\random.jpg");

        JPanel backgroundPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.drawImage(bg1.getImage(), 0, 0, getWidth(), getHeight(), null);
            }
        };

        backgroundPanel.setLayout(new BorderLayout());

        JPanel footerPanel = new JPanel(new BorderLayout());
        footerPanel.setBackground(Color.DARK_GRAY);
        footerPanel.setPreferredSize(new Dimension(frame.getWidth(), 200));

        backgroundPanel.add(footerPanel);
        frame4.add(backgroundPanel, BorderLayout.SOUTH);

        frame4.setVisible(true);
    }

    public class sql {
        public static void main(String[] args) {
            // JDBC URL, username, and password of MySQL server
            String url = "jdbc:mysql://localhost:3306/parking";
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
}