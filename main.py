def read_sheet(sheet_name):
        sheet = workbook[sheet_name]
        data = []

        for row in sheet.iter_rows(values_only=True):
            # Clean the row by replacing None with blank cells
            cleaned_row = [cell if cell is not None else "" for cell in row]
            # Only append rows that have non-empty values
            if any(cleaned_row):
                data.append(cleaned_row)

        # Convert to DataFrame
        df = pd.DataFrame(data)

        return df

    # Display the chosen item's related sheets
    if selected_item:
        # Get the related sheets and link based on the selected item
        related_info = item_to_sheets[selected_item]
        related_sheets = related_info['sheets']
            
        # Read the DataFrames
        df1 = read_sheet(related_sheets[0])
        df2 = read_sheet(related_sheets[1])
        df3 = read_sheet(related_sheets[2])

        # Create a full width container for the DataFrames
        st.write(f"### {related_sheets[0]}")
        st.dataframe(df1, use_container_width=True, hide_index=True)

        st.write(f"### {related_sheets[1]}")
        st.dataframe(df2, use_container_width=True, hide_index=True)
            
        st.write(f"### {related_sheets[2]}")
        st.dataframe(df3, use_container_width=True, hide_index=True)

        # Add link for the selected item
        st.markdown(f"[More about {selected_item}]({related_info['link']})")
