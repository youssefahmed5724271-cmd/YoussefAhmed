  const busData = {
            'cairo-alexandria': [
                { number: 'CA-001', departure: '06:00', arrival: '09:30', company: 'Misr Travel', seats: 45, available: 12, status: 'On Time' },
                { number: 'CA-002', departure: '07:30', arrival: '11:00', company: 'Go Bus', seats: 45, available: 8, status: 'On Time' },
                { number: 'CA-003', departure: '09:00', arrival: '12:30', company: 'East Delta', seats: 45, available: 22, status: 'On Time' },
                { number: 'CA-004', departure: '10:30', arrival: '14:00', company: 'Misr Travel', seats: 45, available: 5, status: 'Arriving Soon' },
                { number: 'CA-005', departure: '13:00', arrival: '16:30', company: 'Go Bus', seats: 45, available: 18, status: 'On Time' },
            ],
            'cairo-suez': [
                { number: 'CS-001', departure: '06:30', arrival: '09:00', company: 'Superjet', seats: 50, available: 15, status: 'On Time' },
                { number: 'CS-002', departure: '08:00', arrival: '10:30', company: 'Go Bus', seats: 50, available: 9, status: 'On Time' },
                { number: 'CS-003', departure: '10:00', arrival: '12:30', company: 'Misr Travel', seats: 50, available: 25, status: 'On Time' },
                { number: 'CS-004', departure: '12:00', arrival: '14:30', company: 'East Delta', seats: 50, available: 3, status: 'Delayed' },
            ],
            'cairo-aswan': [
                { number: 'CA-ASWAN-001', departure: '19:00', arrival: '08:00+1', company: 'Misr Travel', seats: 40, available: 11, status: 'On Time' },
                { number: 'CA-ASWAN-002', departure: '20:00', arrival: '09:30+1', company: 'Go Bus', seats: 40, available: 7, status: 'On Time' },
                { number: 'CA-ASWAN-003', departure: '21:00', arrival: '10:30+1', company: 'Superjet', seats: 40, available: 19, status: 'On Time' },
            ],
            'alexandria-cairo': [
                { number: 'AC-001', departure: '06:00', arrival: '09:30', company: 'East Delta', seats: 45, available: 20, status: 'On Time' },
                { number: 'AC-002', departure: '07:45', arrival: '11:15', company: 'Go Bus', seats: 45, available: 6, status: 'On Time' },
                { number: 'AC-003', departure: '10:00', arrival: '13:30', company: 'Misr Travel', seats: 45, available: 14, status: 'Arriving Soon' },
            ],
            'giza-suez': [
                { number: 'GS-001', departure: '07:00', arrival: '10:00', company: 'Go Bus', seats: 50, available: 17, status: 'On Time' },
                { number: 'GS-002', departure: '09:00', arrival: '12:00', company: 'East Delta', seats: 50, available: 10, status: 'On Time' },
                { number: 'GS-003', departure: '11:00', arrival: '14:00', company: 'Superjet', seats: 50, available: 8, status: 'On Time' },
            ],
            'luxor-aswan': [
                { number: 'LA-001', departure: '08:00', arrival: '12:00', company: 'Go Bus', seats: 40, available: 13, status: 'On Time' },
                { number: 'LA-002', departure: '10:30', arrival: '14:30', company: 'Misr Travel', seats: 40, available: 9, status: 'On Time' },
                { number: 'LA-003', departure: '14:00', arrival: '18:00', company: 'East Delta', seats: 40, available: 21, status: 'On Time' },
            ],
        };

        function getRouteKey(from, to) {
            return `${from}-${to}`;
        }
        function searchBuses() {
            const fromCity = document.getElementById('from-city').value;
            const toCity = document.getElementById('to-city').value;
            const date = document.getElementById('date').value;
            const time = document.getElementById('time').value;

            const resultsTitle = document.getElementById('results-title');
            const busesContainer = document.getElementById('buses-container');
            const noResults = document.getElementById('no-results');
            busesContainer.innerHTML = '';
            noResults.classList.remove('active');

            if (!fromCity || !toCity || fromCity === toCity) {
                alert('Please select different cities');
                return;
            }

            const routeKey = getRouteKey(fromCity, toCity);
            let buses = busData[routeKey] || [];
            if (time) {
                const selectedTime = time.split(':');
                buses = buses.filter(bus => {
                    const depTime = bus.departure.split(':');
                    const depMinutes = parseInt(depTime[0]) * 60 + parseInt(depTime[1]);
                    const selectedMinutes = parseInt(selectedTime[0]) * 60 + parseInt(selectedTime[1]);
                    return depMinutes >= selectedMinutes;
                });
            }

            if (buses.length === 0) {
                noResults.classList.add('active');
                resultsTitle.classList.remove('active');
                return;
            }

            resultsTitle.classList.add('active');
            resultsTitle.textContent = `Available Buses: ${capitalizeCity(fromCity)} → ${capitalizeCity(toCity)}`;

            buses.forEach(bus => {
                const statusClass = bus.status === 'On Time' ? 'coming' : 
                                   bus.status === 'Arriving Soon' ? 'arriving' : 'delayed';
                
                const busCard = document.createElement('div');
                busCard.className = 'bus-card active';
                busCard.innerHTML = `
                    <div class="bus-header">
                        <div class="bus-number">${bus.number}</div>
                        <div class="bus-time">${bus.departure} - ${bus.arrival}</div>
                    </div>
                    <div class="bus-details">
                        <div class="detail-item">
                            <span class="detail-label">Company</span>
                            <span class="detail-value">${bus.company}</span>
                        </div>
                        <div class="detail-item">
                            <span class="detail-label">Seats Available</span>
                            <span class="detail-value">${bus.available} / ${bus.seats}</span>
                        </div>
                        <div class="detail-item">
                            <span class="detail-label">Duration</span>
                            <span class="detail-value">${calculateDuration(bus.departure, bus.arrival)}</span>
                        </div>
                        <div class="detail-item">
                            <span class="detail-label">Status</span>
                            <span class="status ${statusClass}">${bus.status}</span>
                        </div>
                    </div>
                `;
                busesContainer.appendChild(busCard);
            });
        }

        function capitalizeCity(city) {
            const cityNames = {
                'cairo': 'Cairo - القاهرة',
                'giza': 'Giza - الجيزة',
                'alexandria': 'Alexandria - الإسكندرية',
                'suez': 'Suez - السويس',
                'ismailia': 'Ismailia - الإسماعيلية',
                'aswan': 'Aswan - أسوان',
                'luxor': 'Luxor - الأقصر'
            };
            return cityNames[city] || city;
        }

        function calculateDuration(departure, arrival) {
            const [depHours, depMinutes] = departure.split(':').map(Number);
            const [arrHours, arrMinutes] = arrival.split(':').map(Number);
            
            let depTotal = depHours * 60 + depMinutes;
            let arrTotal = arrHours * 60 + arrMinutes;
            if (arrTotal < depTotal) {
                arrTotal += 24 * 60;
            }
            
            const duration = arrTotal - depTotal;
            const hours = Math.floor(duration / 60);
            const mins = duration % 60;
            
            return `${hours}h ${mins}m`;
        }
        window.addEventListener('DOMContentLoaded', function() {
            const today = new Date().toISOString().split('T')[0];
            document.getElementById('date').value = today;
            document.getElementById('time').value = '06:00';
        });
        document.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                searchBuses();
            }
        });
