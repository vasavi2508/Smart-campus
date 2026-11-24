
# Smart Campus Incident and Maintenance Prioritization System

# Severity scores
severity_scores = {
    "critical": 40,
    "high": 30,
    "medium": 20,
    "low": 10
}

# Location scores
location_scores = {
    "laboratory": 30,
    "electrical room": 30,
    "library": 20,
    "classroom": 20,
    "cafeteria": 10,
    "playground": 10,
    "other": 5
}


# Function to calculate frequency score
def calculate_frequency_score(frequency):

    if frequency <= 2:
        return 5

    elif frequency <= 5:
        return 10

    else:
        return 20


# Function to calculate priority score
def calculate_priority(severity, location, frequency):

    severity_score = severity_scores[severity.lower()]

    location_score = location_scores[location.lower()]

    frequency_score = calculate_frequency_score(frequency)

    total_score = (
        severity_score +
        location_score +
        frequency_score
    )

    return total_score, severity_score


# Function to classify priority
def classify_priority(score):

    if score >= 80:
        return "CRITICAL"

    elif score >= 60:
        return "HIGH"

    elif score >= 40:
        return "MEDIUM"

    else:
        return "LOW"


# Function to rank incidents
def rank_incidents(incidents):

    ranked = sorted(
        incidents,
        key=lambda record: (
            record[5],
            record[6],
            record[4]
        ),
        reverse=True
    )

    return ranked


# Main program
print("==============================================")
print(" SMART CAMPUS INCIDENT PRIORITIZATION SYSTEM")
print("==============================================")

incidents = []
incident_ids = []

n = int(input("Enter number of maintenance reports: "))

if n <= 0:

    print("Please enter a valid number of reports.")

else:

    # Collect incident details
    for i in range(n):

        print("\nEnter details for Incident", i + 1)

        incident_id = input("Enter Incident ID: ")

        if incident_id in incident_ids:
            print("Duplicate incident ID. Record rejected.")
            continue

        description = input("Enter problem description: ")

        severity = input(
            "Enter severity (Low/Medium/High/Critical): "
        ).lower()

        location = input(
            "Enter location (Laboratory/Electrical Room/"
            "Library/Classroom/Cafeteria/Playground/Other): "
        ).lower()

        try:
            frequency = int(
                input("Enter number of reports received: ")
            )

        except ValueError:
            print("Invalid frequency. Record rejected.")
            continue

        # Validate input
        if severity not in severity_scores:
            print("Invalid severity. Record rejected.")
            continue

        if location not in location_scores:
            print("Invalid location. Record rejected.")
            continue

        if frequency <= 0:
            print("Frequency must be positive. Record rejected.")
            continue

        # Calculate priority
        score, severity_score = calculate_priority(
            severity, location, frequency
        )

        priority = classify_priority(score)

        # Store incident as a tuple
        record = (
            incident_id,
            description,
            severity,
            location,
            frequency,
            score,
            severity_score,
            priority
        )

        incidents.append(record)
        incident_ids.append(incident_id)

    # Rank incidents
    ranked_incidents = rank_incidents(incidents)

    # Display priority ranking
    print("\n==============================================")
    print("          INCIDENT PRIORITY RANKING")
    print("==============================================")

    for i in range(len(ranked_incidents)):

        record = ranked_incidents[i]

        print("\nPriority Rank:", i + 1)
        print("Incident ID:", record[0])
        print("Description:", record[1])
        print("Severity:", record[2].upper())
        print("Location:", record[3].title())
        print("Reported Frequency:", record[4])
        print("Priority Score:", record[5])
        print("Priority Level:", record[7])

    # Initialize summary counters
    critical_count = 0
    high_count = 0
    medium_count = 0
    low_count = 0

    # Count incidents by priority
    for record in ranked_incidents:

        if record[7] == "CRITICAL":
            critical_count += 1

        elif record[7] == "HIGH":
            high_count += 1

        elif record[7] == "MEDIUM":
            medium_count += 1

        else:
            low_count += 1

    # Display summary
    print("\n==============================================")
    print("              PRIORITY SUMMARY")
    print("==============================================")

    print("Total Valid Incidents:", len(ranked_incidents))
    print("Critical Priority:", critical_count)
    print("High Priority:", high_count)
    print("Medium Priority:", medium_count)
    print("Low Priority:", low_count)

    if len(ranked_incidents) > 0:

        print("\nFirst Incident to Resolve:")
        print("Incident ID:", ranked_incidents[0][0])
        print("Description:", ranked_incidents[0][1])
        print("Priority:", ranked_incidents[0][7])

    print("\n==============================================")
    print("Incident analysis completed successfully.")
    print("==============================================")
