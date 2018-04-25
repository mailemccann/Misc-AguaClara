# Acceleration
# L = length of major losses, h_drive
# v_f = velocity of flow when plate is completely open
# k = constant for major and minor loss coefficients
t = np.linspace(1., 500., 2000)  # 500 seconds, 4 intervals a second
H = 5  # Arbitrary
k = 10  # Arbitrary
k = (2*g*H)/(L*v_f ^ 2)
v = sqrt(2*g*H/k)*tanh(t*sqrt(g*H*k/(2*L)))
plt.plot(t, v)
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.title('Ideal Velocity vs Time')
plt.show()

# Deceleration
# Governing equation is F = ma

# The deceleration of the water after the valve closes is directly proportional
# to the corresponding increase in pressure.
# The pressure spike generated the moment the valve closes will be measured in
# the lab.

# ma = DeltaP(Area)
