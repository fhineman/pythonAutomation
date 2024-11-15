import re

def calc_iperf_data(filename, header):
    """ Parses a test report, which includes an iperf3 report.
    Also finds the iperf3 header, and then calculates the Max, Min, and Avg.

    Args:
        filename: filename of the test report containing the iperf out.
        header: string containing the iperf header.

    Returns:
        A tuple, which contains the Max, Min, & Avg txPut.
    """

    with open(filename, 'r') as fh:
        lines = fh.readlines()
        found_header = False
        txput_values = []

        for line in lines:
            if line.strip() == header:
                found_header = True
                continue

            if found_header:
                match = re.search(r'\d+\.\d+ Gbits/sec', line)
                if match:
                    txput_values.append(float(match.group().split()[0]))

    if txput_values:
        maximum = max(txput_values)
        minimum = min(txput_values)
        average = sum(txput_values) / len(txput_values)

        return maximum, minimum, average
    else:
        return None

filename = "test_report.txt" 
header = "[ ID] Interval           Transfer     Bitrate         Retr  Cwnd"
result = calc_iperf_data(filename, header)

if result:
    maximum, minimum, average = result

    print(" -------------------------------")
    print("|   Test Report: Throughput     |")
    print(" -------------------------------")
    print(f"Maximum Throughput: {maximum:.2f} Gbits/sec")
    print(f"Minimum Throughput: {minimum:.2f} Gbits/sec")
    print(f"Average Throughput: {average:.2f} Gbits/sec")

else:
    print("Test Error: TxPut data NOT found!")
