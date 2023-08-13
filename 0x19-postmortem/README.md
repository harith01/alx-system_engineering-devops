## Postmortem Incidence Report

Summary: On May 10, 2023, our system experienced a service outage that lasted for 2 hours. During this time, our users were unable to access our services, and some data was lost. The root cause of the incident was a hardware failure in one of our data centers.

Timeline (All the times are in EAT time-zone):

8:00 AM: Our monitoring system alerted us to a problem with one of our servers in Data Center A.
8:15 AM: Our team began investigating the issue and discovered that the server had experienced a hardware failure.
8:30 AM: We attempted to fail over to our backup server, but it also failed due to a software issue.
9:00 AM: We escalated the issue to our hardware vendor for further support.
10:30 AM: The hardware vendor replaced the faulty hardware and restored service to the affected server.
10:45 AM: We confirmed that all services were restored and began monitoring the system for any further issues.
Root Cause: The root cause of the incident was a hardware failure in one of our servers in Holberton. The failure was caused by a faulty power supply unit, which resulted in data loss and the subsequent service outage.

Impact: The outage affected all users who were attempting to access our services during the downtime period, resulting in lost productivity and potential revenue. Additionally, some data was lost due to the outage, resulting in data integrity issues.

Resolution: To prevent a similar incident from occurring in the future, we have taken the following actions:

We have replaced the faulty power supply unit and conducted a thorough review of all hardware in Holberton Data Center.
We have implemented an automatic fail over process for our backup server to prevent future service disruptions.
We have updated our incident response procedures to include faster escalation to our hardware vendor for additional support.
Conclusion: We apologize for the inconvenience that this incident caused our users and customers. We take this incident seriously and have taken steps to prevent a similar issue from occurring in the future. We will continue to monitor our systems and improve our incident response procedures to minimize the impact of any future incidents.
