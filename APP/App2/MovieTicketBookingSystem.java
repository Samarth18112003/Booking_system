import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.DecimalFormat;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.SwingUtilities;

public class MovieTicketBookingSystem {
    private JFrame frame;
    private JComboBox<String> movieComboBox;
    private JComboBox<String> timeComboBox;
    private JComboBox<String> locationComboBox;
    private JPanel seatPanel;
    private JButton calculateButton;
    private JTextArea billTextArea;

    private String[] movies = { "Avengers", "Leo", "Jawan", "Tiger", "Annabelle" };
    private String[] times = { "10:00 AM", "1:00 PM", "5:00 PM", "8:00 PM" };
    private String[] locations = { "Anna Nagar", "Guindy", "Tambaram", "Vandalur", "OMR" };

    private double ticketPrice = 120.0;
    private int selectedSeats = 0;

    public MovieTicketBookingSystem() {
        frame = new JFrame("Movie Ticket Booking System");
        frame.setLayout(new GridLayout(2, 1));

        JPanel inputPanel = new JPanel();
        inputPanel.setLayout(new FlowLayout());

        movieComboBox = new JComboBox<>(movies);
        timeComboBox = new JComboBox<>(times);
        locationComboBox = new JComboBox<>(locations);

        inputPanel.add(new JLabel("Movie:"));
        inputPanel.add(movieComboBox);
        inputPanel.add(new JLabel("Time:"));
        inputPanel.add(timeComboBox);
        inputPanel.add(new JLabel("Location:"));
        inputPanel.add(locationComboBox);

        frame.add(inputPanel);

        seatPanel = new JPanel();
        seatPanel.setLayout(new GridLayout(5, 5));

        // Create seat buttons and add action listeners
        for (int i = 1; i <= 25; i++) {
            JButton seatButton = new JButton("Seat " + i);
            seatButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    JButton button = (JButton) e.getSource();
                    if (button.getBackground() == Color.GREEN) {
                        button.setBackground(null);
                        selectedSeats--;
                    } else {
                        button.setBackground(Color.GREEN);
                        selectedSeats++;
                    }
                }
            });
            seatPanel.add(seatButton);
        }

        frame.add(seatPanel);

        calculateButton = new JButton("Calculate");
        calculateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                calculateTotalPrice();
            }
        });

        billTextArea = new JTextArea(10, 40);
        billTextArea.setEditable(false);

        frame.add(calculateButton);
        frame.add(billTextArea);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }

    private void calculateTotalPrice() {
        double totalPrice = selectedSeats * ticketPrice;

        String selectedMovie = movieComboBox.getSelectedItem().toString();
        String selectedTime = timeComboBox.getSelectedItem().toString();
        String selectedLocation = locationComboBox.getSelectedItem().toString();

        DecimalFormat df = new DecimalFormat("#.00");

        String bill = "Movie: " + selectedMovie + "\n" +
                "Time: " + selectedTime + "\n" +
                "Location: " + selectedLocation + "\n" +
                "Selected Seats: " + selectedSeats + "\n" +
                "Total Price: Rs." + df.format(totalPrice);

        billTextArea.setText(bill);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new MovieTicketBookingSystem();
            }
        });
    }
}
