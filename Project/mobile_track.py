
import streamlit as st
import phonenumbers
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Mobile Location Finder",
    page_icon="📍",
    layout="wide"
)

st.title("📍 Mobile Location Finder")
st.write("Authorized GPS Location Viewer")

mobile = st.text_input(
    "Enter Mobile Number",
    placeholder="+91XXXXXXXXXX"
)

if st.button("Validate Number"):

    try:
        number = phonenumbers.parse(mobile, "IN")

        if phonenumbers.is_valid_number(number):

            st.success("Valid Mobile Number")

            st.write(
                "International Number:",
                phonenumbers.format_number(
                    number,
                    phonenumbers.PhoneNumberFormat.INTERNATIONAL
                )
            )

            st.info(
                "Mobile number verified for format only. "
                "GPS location requires separate user consent."
            )

        else:
            st.error("Invalid Mobile Number")

    except Exception as e:
        st.error(str(e))

st.divider()

st.subheader("🌍 Authorized GPS Location")

# latitude = st.number_input(
#     "Latitude",
#     value=28.4595,
#     format="%.6f"
# )

# longitude = st.number_input(
#     "Longitude",
#     value=77.0266,
#     format="%.6f"
# )

# if st.button("Show Location on Map"):

#     location_map = folium.Map(
#         location=[latitude, longitude],
#         zoom_start=15
#     )

#     folium.Marker(
#         [latitude, longitude],
#         popup="Authorized GPS Location",
#         tooltip="View Location"
#     ).add_to(location_map)

#     st_folium(
#         location_map,
#         width=900,
#         height=500
#     )

#     st.markdown(
#         f"[Open Location in Google Maps](https://www.google.com/maps?q={latitude},{longitude})"
#     )

st.title("📍 Location Map")

latitude = st.number_input(
    "Latitude",
    value=28.4595
)

longitude = st.number_input(
    "Longitude",
    value=77.0266
)

# Initialize session state
if "show_map" not in st.session_state:
    st.session_state.show_map = False

if st.button("Show Location on Map"):
    st.session_state.show_map = True

# Display map
if st.session_state.show_map:

    location_map = folium.Map(
        location=[latitude, longitude],
        zoom_start=15
    )

    folium.Marker(
        [latitude, longitude],
        popup="Authorized GPS Location",
        tooltip="View Location"
    ).add_to(location_map)

    st_folium(
        location_map,
        width=900,
        height=500,
        key="location_map"
    )

    st.markdown(
        f"https://www.google.com/maps?q={latitude},{longitude}"
    )
